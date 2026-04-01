package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A collection of Elements that have a shared context.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Bundle extends ElementCollection {

  private String context;

}