package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Provides an independently reproducible mechanism that permits verification of a specific Element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class IntegrityMethod  {

  private String comment;

}