package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A mathematically calculated representation of a grouping of data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Hash extends IntegrityMethod {

  private String algorithm;
  private String hashValue;

}