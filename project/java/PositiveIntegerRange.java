package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A tuple of two positive integers that define a range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PositiveIntegerRange  {

  private int endIntegerRange;
  private int beginIntegerRange;

}